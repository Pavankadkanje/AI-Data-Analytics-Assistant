import plotly.express as px


def bar_chart(df, x, y):
    return px.bar(df, x=x, y=y)


def line_chart(df, x, y):
    return px.line(df, x=x, y=y)


def scatter_chart(df, x, y):
    return px.scatter(df, x=x, y=y)


def histogram(df, column):
    return px.histogram(df, x=column)


def pie_chart(df, column):
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, "Count"]
    return px.pie(counts, names=column, values="Count")


def box_plot(df, column):
    return px.box(df, y=column)


def correlation_heatmap(df):
    numeric = df.select_dtypes(include="number")
    corr = numeric.corr()

    return px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Viridis",
        aspect="auto"
    )