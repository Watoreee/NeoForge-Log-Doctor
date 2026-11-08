# Architecture

Diagram source for the report (Mermaid; GitHub renders it). Every box names the module that implements it.

## Request path (the app)

```mermaid
flowchart TD
    U["Browser<br/>web/index.html + web/sse.js<br/>(fetch + ReadableStream)"]
    API["api.py<br/>POST /diagnose, GET /health<br/>size cap 10 MB -> 413, not a log -> 422"]
    SVC["service.py<br/>default_pipeline"]
    RED["redact.py<br/>player name, UUID, tokens, IPs, user folders"]
    PRE["preprocess.py<br/>regex facts + trim to ~6,000 tokens<br/>(truncated, original_bytes)"]
    EXT["extraction.py<br/>LLM -> LogFacts (pydantic)<br/>suspect ids must be whole tokens of the log"]
    LOOP["agent/loop.py<br/>JSON text protocol, max 5 tool rounds,<br/>then a forced final answer"]
    TOOLS["agent/tools.py<br/>allow-list + pydantic args (extra=forbid)<br/>output wrapped as untrusted data"]
    SD["search_docs"]
    GMI["get_mod_info<br/>(what this log says about a mod)"]
    CC["check_compat<br/>(agent/compat_table.py)"]
    IDX["retrieval/index.py<br/>BM25 + dense (bge-m3), cosine floor 0.45,<br/>RRF k=60"]
    DIAG["diagnosis.py<br/>Diagnosis (pydantic): culprit, category,<br/>explanation, fix steps, citations, confidence<br/>citations limited to retrieved docs; one repair, then fallback"]
    LLM["llm.py<br/>gemma-4-E4B-it + bge-m3 via the class proxy<br/>disk cache eval/cache, replay mode"]
    CORPUS[("data/processed/<br/>689 docs, chunks + embeddings")]

    U -- "log text" --> API --> SVC --> RED --> PRE --> EXT --> LOOP
    LOOP -- "tool call" --> TOOLS
    TOOLS --> SD --> IDX --> CORPUS
    TOOLS --> GMI
    TOOLS --> CC
    TOOLS -- "tool result" --> LOOP
    LOOP -- "final JSON" --> DIAG
    EXT -. "chat" .-> LLM
    LOOP -. "chat" .-> LLM
    IDX -. "embed query" .-> LLM
    SVC -- "SSE: facts, tool_call, tool_result, final / error" --> U
```

The page shows progress events as they arrive. Only structured events are streamed, never raw model tokens. Model
text is inserted with `textContent`.

## Offline: corpus, labels, evaluation

```mermaid
flowchart LR
    GH["GitHub issues + releases<br/>(22 repos)"] --> FETCH["scripts/fetch_corpus.py"]
    ND["NeoForge 1.21.1 docs"] --> FETCH
    FETCH --> RAW[("data/raw/")] --> BUILD["scripts/build_index.py<br/>retrieval/chunking.py"] --> PROC[("data/processed/")]

    INST["Fault-injected modpack runs<br/>(raw logs kept outside the repo)"] --> COLLECT["scripts/collect_run.py"] --> REDACT["scripts/redact_logs.py<br/>(redact.py) -> data/staging/,<br/>read by the author"] --> GOLD[("data/gold/<br/>7 dev + 25 test logs")]
    PROC --> POOL["scripts/export_relevance_pool.py"] --> SHEETS[("data/pool/ sheets<br/>LLM-judged relevance")] --> APPLY["scripts/apply_judgments.py"] --> GOLD

    GOLD --> EVAL["scripts/run_eval.py<br/>B0, B1, RAG-1 (rag.py), Agent"]
    GOLD --> REVAL["scripts/run_retrieval_eval.py<br/>queries (a), (b), (c), (c2), B2"]
    PROC --> EVAL
    PROC --> REVAL
    EVAL --> RES[("eval/results/")]
    REVAL --> RES
    RES --> TABLES["scripts/report_tables.py<br/>tables + paired bootstrap"]
```

The evaluation scripts call the pipeline functions directly (`preprocess_log`, `extract_facts`, `rag1`, `run_agent`),
not the HTTP API. With `CRASHDOC_REPLAY=1` every LLM and embedding call is served from `eval/cache/`, so the numbers
reproduce without a key.
