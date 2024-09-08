from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add nodes with different colors for clarity
dot.node('A', 'Fetch Content from Website', shape='box', style='filled', color='lightblue')
dot.node('B', 'Extract and Chunk Text', shape='box', style='filled', color='lightgreen')
dot.node('C', 'Generate Embeddings', shape='box', style='filled', color='lightyellow')
dot.node('D', 'Store in FAISS Vector Store', shape='box', style='filled', color='lightcoral')
dot.node('E', 'Query FAISS Index', shape='box', style='filled', color='lightgray')
dot.node('F', 'Simplify Content (Technical Writer)', shape='box', style='filled', color='lightpink')
dot.node('G', 'Review Content (Senior Editor)', shape='box', style='filled', color='lightgreen')
dot.node('H', 'Final Revised Content', shape='box', style='filled', color='lightyellow')

# Add edges between nodes
dot.edge('A', 'B', label='1. Fetch website content')
dot.edge('B', 'C', label='2. Chunk content into texts')
dot.edge('C', 'D', label='3. Generate embeddings')
dot.edge('D', 'E', label='4. Store embeddings')
dot.edge('E', 'F', label='5. Query FAISS index')
dot.edge('F', 'G', label='6. Simplify content')
dot.edge('G', 'H', label='7. Review and revise content')

# Interactions between Technical Writer and Senior Editor
dot.edge('G', 'F', label='8. Provide feedback to Technical Writer', style='dashed', color='blue')
dot.edge('F', 'G', label='9. Review feedback, improve content', style='dashed', color='blue')
dot.edge('F', 'H', label='10. Submit final version', style='dashed', color='blue')

# Save and render the diagram
dot.render('updated_content_processing_flow', format='png', cleanup=True)

# Optionally, display the generated image
from PIL import Image
img = Image.open('updated_content_processing_flow.png')
img.show()
