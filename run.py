from app import create_app

app = create_app()
app.secret_key = 'SGVsbG8gdGhlcmUgIQ=='

if __name__ == '__main__':
    app.run(debug=True)