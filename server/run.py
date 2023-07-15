from app import create_app
from app import db
from populate_database import create_all, create_extension
from werkzeug.security import generate_password_hash, check_password_hash
import os

from app import model

# Instance of flask app
app = create_app("production")


@app.shell_context_processor
def make_shell_context():
    """Makes all the dictionary element available to
    the terminal shell
    """
    return dict(db=db,
                clear=lambda: os.system('cls'),
                create_all=create_all,
                create_extension=create_extension,
                model=model,
                generate_password_hash=generate_password_hash,
                check_password_hash=check_password_hash)



if __name__ == "__main__":
    app.run()
