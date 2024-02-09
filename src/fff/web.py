import io
import logging
import textwrap
import time

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

from yarl import URL

from fff.app import from_grpc, generate_png, get_username


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@app.get("/")
def root(request: Request):
    """
    Just a splash screen with the action button
    """

    base_url = str(request.base_url)
    banner_url = URL(base_url) / "static" / "banner-square.png"
    followers_url = URL(base_url) / "followers"
    followers_label = "get my data"

    return HTMLResponse(
        status_code=200,
        content=textwrap.dedent(
            f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Got followers?</title>
                    <meta property="og:title" content="Got followers?" />
                    <meta property="og:image" content="{banner_url}" />
                    <meta property="fc:frame:image" content="{banner_url}" />
                    <meta property="fc:frame" content="vNext" />
                    <meta property="fc:frame:button:1" content="{followers_label}" />
                    <meta property="fc:frame:button:2" content="Github" />
                    <meta property="fc:frame:button:2:action" content="link" />
                    <meta property="fc:frame:button:2:target" content="https://github.com/karmacoma-eth/farcaster-followers-frame" />
                    <meta property="fc:frame:post_url" content="{followers_url}" />
                </head>
                <body>
                    <div>
                        <img src="{banner_url}" alt="Got followers?" style="width: 100%; max-width: 1024px;">
                    </div>
                    <form action="{followers_url}" method="post">
                        <input type="text" name="fid" placeholder="fid">
                        <input type="submit" value="{followers_label}">
                    </form>
                </body>
            </html>
        """
        ),
    )


@app.get("/followers") # for local testing
@app.post("/followers") # for actual Frame usage
async def followers(request: Request, fid: int = None):
    """
    Get the follower data
    """

    base_url = str(request.base_url)

    content_type = request.headers.get("content-type")
    ts = int(time.time())

    if content_type == "application/json":
        body = await request.json()
        fid: int = body["untrustedData"]["fid"]

    elif content_type == "application/x-www-form-urlencoded":
        body = await request.form()
        print(body)
        fid = int(body.get("fid"))

    else:
        return HTMLResponse(
            status_code=400,
            content="Invalid content type",
        )

    if not fid:
        return HTMLResponse(
            status_code=400,
            content="No fid provided",
        )

    followers_url = URL(base_url) / "followers"

    # add the timestamp to the URL to bust any caches
    followers_image_url = URL(base_url) / "followers_image" / f"{fid}" % {'ts': ts}

    return HTMLResponse(
        status_code=200,
        content=textwrap.dedent(
            f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Got followers?</title>
                    <meta property="og:title" content="Got followers?" />
                    <meta property="og:image" content="{followers_image_url}" />
                    <meta property="fc:frame:image" content="{followers_image_url}" />
                    <meta property="fc:frame:image:aspect_ratio" content="1:1" />
                    <meta property="fc:frame" content="vNext" />
                    <meta property="fc:frame:button:1" content="Reload" />
                    <meta property="fc:frame:post_url" content="{followers_url}" />
                </head>
                <body>
                    <div>
                        <img src="{followers_image_url}" alt="Got followers?" style="width: 100%; max-width: 1024px;">
                    </div>
                </body>
            </html>
        """),
    )


@app.get("/followers_image/{fid}")
async def followers_image(fid: int, request: Request):
    """
    Get the follower data as an image
    """

    data = from_grpc(fid)
    username = get_username(fid)
    png = generate_png(data, f"@{username}'s followers")

    return StreamingResponse(io.BytesIO(png.getvalue()), media_type="image/png")
