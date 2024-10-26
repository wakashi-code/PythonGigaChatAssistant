from IPython.display import Image, display
import traceback

try:
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
except Exception as ex:
    traceback.format_exc()
    # This requires some extra dependencies and is optional
    pass

from pprint import pprint

# Run
inputs = {
    "question": "Какие есть терапевты?"
}
for output in app.stream(inputs):
    for key, value in output.items():
        # Node
        pprint(f"Node '{key}':")
        # Optional: print full state at each node
        # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
    pprint("\n---\n")

# Final generation
pprint(value["generation"])