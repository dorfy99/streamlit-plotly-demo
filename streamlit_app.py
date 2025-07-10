import streamlit as st
import plotly.graph_objects as go

# Schieberegler für Gerade 1
m1 = st.slider("Steigung m1", -10.0, 10.0, 1.0)
b1 = st.slider("y-Achsenabschnitt b1", -10.0, 10.0, 0.0)

# Schieberegler für Gerade 2
m2 = st.slider("Steigung m2", -10.0, 10.0, -1.0)
b2 = st.slider("y-Achsenabschnitt b2", -10.0, 10.0, 2.0)

# x-Werte
x = list(range(-10, 11))
y1 = [m1 * xi + b1 for xi in x]
y2 = [m2 * xi + b2 for xi in x]

# Diagramm mit Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Gerade 1'))
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Gerade 2'))
fig.update_layout(title='Zwei Geraden', xaxis_title='x', yaxis_title='y')

st.plotly_chart(fig)
