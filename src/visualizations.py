import plotly.graph_objects as go
import pandas as pd

def map_properties(status):
        if status in ['no', 'out', 'out of scope', 'false']:
            return 3, "#e74c3c", "OUT OF SCOPE"
        elif status in ['boundary', 'partial', 'maybe']:
            return 2, "#f1c40f", "SCOPE BOUNDARY"
        else:
            return 1, "#2ecc71", "IN SCOPE"


def create_control_wheel(df_subset, group_name):
    
    # Mapping properties
    props = df_subset['Status'].apply(map_properties)
    df_subset['Radius'] = [p[0] for p in props]
    df_subset['Color'] = [p[1] for p in props]
    df_subset['Label'] = [p[2] for p in props]

    fig = go.Figure()

    for i in range(len(df_subset)):
        var_name = df_subset['Variable'].iloc[i]
        hover_text = (f"<b>{var_name} - {df_subset['Control_Name'].iloc[i]}</b><br>"
                      f"Status: {df_subset['Label'].iloc[i]}<br>"
                      f"Score: {df_subset['Score/5'].iloc[i]}/5")

        fig.add_trace(go.Scatterpolar(
            r=[0, df_subset['Radius'].iloc[i]],
            theta=[var_name, var_name],
            mode='lines+markers',
            marker=dict(size=[0, 10], color=df_subset['Color'].iloc[i]),
            line=dict(color=df_subset['Color'].iloc[i], width=4),
            hoverinfo='text',
            text=[hover_text, hover_text],
            showlegend=False
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 3.2], showticklabels=False),
            angularaxis=dict(direction='clockwise')
        ),
        title=dict(text=f"Security Control Status Wheel: {group_name}", x=0.5),
        height=700
    )
    return fig