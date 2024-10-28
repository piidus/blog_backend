from website import create_app
from website import log

app = create_app()


if __name__ == '__main__':
    app.run(port=4000, debug=True)
    # app
    
    

    