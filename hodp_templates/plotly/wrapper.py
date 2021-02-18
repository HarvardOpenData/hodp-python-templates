import plotly.graph_objects as go
from .template import hodp_theme, primary_colors


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
            marker_color=primary_colors[i % 5],
        ))

    fig.update_layout(title=title,
                      xaxis={'title': {'text': labels[x] if x in labels else x}},
                      yaxis={'title': {'text': labels[y] if y in labels else y}},
                      legend={'title': {'text': labels[line_group] if line_group in labels else line_group}},
                      template=hodp_theme)

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
            marker_color=primary_colors[i % 5],
        ))

    fig.update_layout(title=title,
                      xaxis={'title': {'text': labels[x] if x in labels else x}},
                      yaxis={'title': {'text': labels[y] if y in labels else y}},
                      legend={'title': {'text': labels[line_group] if line_group in labels else line_group}},
                      template=hodp_theme)

    return fig


def bar(data_frame, x, y, line_group, labels, title, barmode='group'):
    fig = go.Figure()

    categories = data_frame[line_group].unique()

    for i, category in enumerate(categories):
        df = data_frame[data_frame[line_group] == category]
        fig.add_trace(go.Bar(
            x=df[x],
            y=df[y],
            hovertext=[f"<b>{labels[x] if x in labels else x}</b>={df[x][i]}<br>" for i in range(len(df))],
            name=category,
            marker_color=primary_colors[i % 5],
        ))

    fig.update_layout(title=title,
                      xaxis={'title': {'text': labels[x] if x in labels else x}},
                      yaxis={'title': {'text': labels[y] if y in labels else y}},
                      legend={'title': {'text': labels[line_group] if line_group in labels else line_group}},
                      template=hodp_theme,
                      barmode=barmode)

    return fig
