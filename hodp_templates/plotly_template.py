import plotly.graph_objects as go

# colors
monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

# template
hodp_theme = go.layout.Template(
    layout=go.Layout(
        title={
            'font': {
                'size': 24,
                'family': "Helvetica",
                'color': monochrome_colors[0]
            },
            'pad': {
                't': 100,
                'r': 0,
                'b': 0,
                'l': 0
            }
        },
        font={
            'size': 18,
            'family': 'Helvetica',
            'color': '#717171'
        },
        xaxis={
            'ticks': "outside",
            'tickfont': {
                'size': 14,
                'family': "Helvetica"
            },
            'showticksuffix': 'all',
            'showtickprefix': 'last',
            'showline': True,
            'title': {
                'font': {
                    'size': 18,
                    'family': 'Helvetica'
                },
                'standoff': 20
            },
            'automargin': True
        },
        yaxis={
            'ticks': "outside",
            'tickfont': {
                'size': 14,
                'family': "Helvetica"
            },
            'showticksuffix': 'all',
            'showtickprefix': 'last',
            'title': {
                'font': {
                    'size': 18,
                    'family': 'Helvetica'
                },
                'standoff': 20
            },
            'showline': True,
            'automargin': True
        },
        legend={
            'bgcolor': 'rgba(0,0,0,0)',
            'title': {
                'font': {
                    'size': 18,
                    'family': "Helvetica",
                    'color': monochrome_colors[0]
                }
            },
            'font': {
                'size': 14,
                'family': "Helvetica"
            },
            'yanchor': 'bottom'
        },
        colorscale={'diverging': monochrome_colors},
        coloraxis={
            'autocolorscale': True,
            'cauto': True,
            'colorbar': {
                'tickfont': {
                    'size': 14,
                    'family': 'Helvetica'
                },
                'title': {
                    'font': {
                        'size': 18,
                        'family': 'Helvetica'
                    }
                }
            },
        }
    )
)
