import kagglehub

resolved = kagglehub.resolve("dissfya/atp-tennis-daily-pull")
print("✅ Dataset files:")
print(resolved["files"])