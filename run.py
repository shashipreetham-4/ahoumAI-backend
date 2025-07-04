from app import create_app

print("✅ run.py started")

app = create_app()
print("✅ App created")

if __name__ == "__main__":
    app.run(debug=True)
