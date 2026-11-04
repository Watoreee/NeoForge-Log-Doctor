// Minimal Server-Sent Events parser for fetch() + ReadableStream (EventSource cannot POST a body).
// push(text) accepts arbitrary chunk boundaries; onEvent({event, data}) fires once per complete event.
function createSseParser(onEvent) {
  let buffer = "";
  function dispatch(block) {
    let event = "message";
    const data = [];
    for (const line of block.split("\n")) {
      if (!line || line.startsWith(":")) continue;
      const i = line.indexOf(":");
      const field = i === -1 ? line : line.slice(0, i);
      const value = i === -1 ? "" : line.slice(i + 1).replace(/^ /, "");
      if (field === "event") event = value;
      else if (field === "data") data.push(value);
    }
    if (data.length) onEvent({ event, data: data.join("\n") });
  }
  return {
    push(text) {
      buffer += text.replace(/\r\n/g, "\n");
      let end;
      while ((end = buffer.indexOf("\n\n")) !== -1) {
        dispatch(buffer.slice(0, end));
        buffer = buffer.slice(end + 2);
      }
    },
  };
}
if (typeof module !== "undefined") module.exports = { createSseParser };
