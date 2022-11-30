# make sure to install the below libraries for the function to work
# pip install plotly.express
# pip install plotly.graph_objects
# pip install PIL
# pip install io

import plotly.express as px
import plotly.graph_objects as go
import PIL
import io


def make_gif_plotly(fig, fname):
    '''
    function that converts an animated plotly plot into a gif
    :param fig: plotly interactive animated plot
    :param fig type: ploty.graph_objects.Figure
    :param fname: file path where the gif should be stored
    :param fig type: string
    :rtype: None
    '''
    assert isinstance(fig, go.Figure)
    assert isinstance(fname, str)
    assert fname.endswith('.gif')

    frames = []
    for s, fr in enumerate(fig.frames):
        # set main traces to appropriate traces within plotly frame
        fig.update(data=fr.data)
        # move slider to correct place
        fig.layout.sliders[0].update(active=s)
        # generate image of current state
        frames.append(PIL.Image.open(io.BytesIO(fig.to_image(format="png"))))
    # save the frames into the file location provided
    frames[0].save(
        fname,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=200,
        loop=0,
    )


# EXAMPLE CALL TO THE FUNCTION
# df = px.data.gapminder()  # inbuilt dataframe
# fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#                  size="pop", color="continent", hover_name="country",
#                  log_x=True, size_max=55, range_x=[100, 100000], range_y=[25, 90])
# fname = "test.gif"
# make_gif_plotly(fig, fname)
