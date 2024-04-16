font = "relative-mono-11-pitch-pro, Menlo, monospace"
labelfont = "relative-mono-11-pitch-pro, Menlo, monospace"
sourcefont = "relative-mono-11-pitch-pro, Menlo, monospace"


def theme(colors):
    markColor = colors["text"]
    axisColor = colors["text"]
    gridColor = colors["grey"]
    backgroundColor = colors["background"]
    fontWeight = 400
    symbolSize = 200

    axis = {
        "domainColor": gridColor,
        "gridColor": gridColor,
        "tickColor": gridColor,
        "labelFont": labelfont,
        "titleFont": font,
        "labelColor": axisColor,
        "titleColor": axisColor,
    }

    return {
        "config": {
            "arc": {"fill": markColor},
            "area": {"fill": markColor},
            "axisX": {"grid": False},
            "axisY": {"grid": False},
            "axisBottom": axis,
            "axisLeft": axis,
            "view": {"stroke": None},
            "background": backgroundColor,
            "group": {"fill": backgroundColor},
            "legend": {
                "labelFont": labelfont,
                "symbolSize": symbolSize,
                "symbolType": "circle",
                "titleFont": font,
            },
            "line": {"color": markColor, "stroke": markColor},
            "trail": {"color": markColor, "stroke": markColor},
            "path": {"stroke": markColor},
            "point": {
                "filled": True,
                "color": markColor,
                "size": symbolSize,
                "cursor": "pointer",
            },
            "range": {
                "category": [
                    colors[c]
                    for c in [
                        "blue",
                        "orange",
                        "green",
                        "red",
                        "purple",
                        "pink",
                        "grey",
                        "yellow",
                        "teal",
                    ]
                ],
                # TODO.
                #    "diverging": [
                #        "#dc0d12",
                #        "#e9686b",
                #        "#fbe1e1",
                #        "#dff4f9",
                #        "#81d1e6",
                #        "#03a3cd"
                #    ],
                #    "heatmap": [
                #        "#fcdfef",
                #        "#f8bfde",
                #        "#f59fce",
                #        "#f180be",
                #        "#ee60ad",
                #        "#eb409d",
                #        "#e7208c",
                #        "#e4007c",
                #    ],
            },
            "symbol": {"shape": "circle"},
            "style": {
                "bar": {"fill": markColor},
                "text": {"font": sourcefont, "fontWeight": fontWeight},
            },
            "title": {"anchor": "start", "fontWeight": fontWeight, "font": font},
            "header": {
                "fontWeight": fontWeight,
                "labelFont": labelfont,
                "titleFont": font,
            },
        },
    }


def dark():
    """CarbonPlan dark theme entrypoint"""
    from .colors import dark

    return theme(dark)


def light():
    """CarbonPlan light theme entrypoint"""
    from .colors import light

    return theme(light)
