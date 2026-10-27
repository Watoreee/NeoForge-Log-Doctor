"""Pydantic schemas shared across the app. Day 1: the gold-label schema (PLAN 6.1)."""

from __future__ import annotations

from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, model_validator


class Category(StrEnum):
    """Error categories. Conditional ones (java_version, gpu_native) are dropped if they end up with 0 logs."""

    MISSING_DEPENDENCY = "missing_dependency"
    VERSION_MISMATCH = "version_mismatch"
    DUPLICATE_MOD = "duplicate_mod"
    MIXIN_CONFLICT = "mixin_conflict"
    OUT_OF_MEMORY = "out_of_memory"
    CONFIG_ERROR = "config_error"
    JAVA_VERSION = "java_version"
    GPU_NATIVE = "gpu_native"
    OTHER = "other"


SourceFileType = Literal["crash_report", "latest_log", "debug_log", "hs_err"]
SupportSearch = Literal["none_found", "uncertain"]


class GoldLabel(BaseModel):
    """One label file per gold log. The per-label rules are enforced here; cross-log rules in labels.py."""

    model_config = ConfigDict(extra="forbid")

    log_id: str
    scenario_id: str
    source_file_type: SourceFileType
    culprit_mod_id: str | None
    acceptable_culprits: list[str]
    category: Category
    # None = relevance not judged yet (Day 3-4). [] = judged, nothing relevant.
    relevant_doc_ids: list[str] | None = None
    support_search: SupportSearch | None = None
    notes: str = ""

    @model_validator(mode="after")
    def _culprit_rules(self) -> GoldLabel:
        """Scoring checks only acceptable_culprits, so it must contain the culprit (and nothing for null)."""
        if self.culprit_mod_id is None and self.acceptable_culprits:
            raise ValueError("culprit_mod_id is null, so acceptable_culprits must be []")
        if self.culprit_mod_id is not None and self.culprit_mod_id not in self.acceptable_culprits:
            raise ValueError(f"acceptable_culprits must include culprit_mod_id {self.culprit_mod_id!r}")
        return self

    @model_validator(mode="after")
    def _support_search_rules(self) -> GoldLabel:
        """Both directions: empty relevant_doc_ids <=> support_search is set."""
        if self.relevant_doc_ids is None:
            if self.support_search is not None:
                raise ValueError("support_search is set but relevant_doc_ids has not been judged (null)")
        elif not self.relevant_doc_ids and self.support_search is None:
            raise ValueError('relevant_doc_ids is [], so support_search must be "none_found" or "uncertain"')
        elif self.relevant_doc_ids and self.support_search is not None:
            raise ValueError("relevant_doc_ids is non-empty, so support_search must be null")
        return self

    @property
    def relevance_judged(self) -> bool:
        return self.relevant_doc_ids is not None
