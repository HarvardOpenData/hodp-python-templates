import plotly.graph_objects as go
import template as tmp


def line(data_frame, x, y, line_group, labels, title):
    fig = go.Figure()

    categories = data_frame[line_group].unique()

    for i, category in enumerate(categories):
        df = data_frame[data_frame[line_group] == category]
        fig.add_trace(go.Scatter(
            x=df[x],
            y=df[y],
            name=category,
            mode='lines+markers',
            marker_color=tmp.primary_colors[i % 5],
        ))

    fig.update_layout(title=title,
                      xaxis={'title': {'text': labels[x]}},
                      yaxis={'title': {'text': labels[y]}},
                      legend={'title': {'text': labels[line_group]}},
                      template=tmp.hodp_theme)

    return fig


def scatter(data_frame, x, y, line_group, labels, title):
    fig = go.Figure()

    categories = data_frame[line_group].unique()

    for i, category in enumerate(categories):
        df = data_frame[data_frame[line_group] == category]
        fig.add_trace(go.Scatter(
            x=df[x],
            y=df[y],
            name=category,
            mode='markers',
            marker_color=tmp.primary_colors[i % 5],
        ))

    fig.update_layout(title=title,
                      xaxis={'title': {'text': labels[x]}},
                      yaxis={'title': {'text': labels[y]}},
                      legend={'title': {'text': labels[line_group]}},
                      template=tmp.hodp_theme)

    return fig
