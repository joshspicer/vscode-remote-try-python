
#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route("/")
def hello():
    data = {}
    arr = pd.DataFrame(data)
    return app.send_static_file("index.html")
