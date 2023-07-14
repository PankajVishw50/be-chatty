from . import avatar
from .model import generate_multiavatar
from uuid import uuid4

from flask import render_template_string


@avatar.route("/random-avatar")
def get_random():
    html = """
<!DOCTYPE html>
<html>
  <head>
    <title>SVG Image Example</title>
    <style>
    *{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    }
      .container {
        height: 100vh;
        width: 100vw;
        padding: 20px;
        display: flex;
        align-items: center; /* Center the SVG vertically */
        justify-content: center; /* Center the SVG horizontally */
      }

      .svg-wrapper {
        width: 500px;
        height: 500px;
        max-width: 100%; /* Allow the SVG to shrink to fit the container */
        overflow: hidden; /* Hide any overflow of the SVG */
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="svg-wrapper">
        {{ data | safe }}
      </div>
    </div>
  </body>
</html>
    """
    # file = generate_multiavatar(uuid4())
    # file.replace("viewbox=\"*[")
    return render_template_string(html, data=generate_multiavatar(uuid4()))