# Deploy 🚀

Currently, our deployment is executed by a human being.
Fear not, this is a step-by-step to guide you through it.
Ready?

## Checklist

1. Pull the code from the `main` branch
2. Configure the environment
    1. Configure the environment variables in the `.env` file
    2. Install the dependencies with:

```bash
pip install -r requirements.txt
```

3. Run the migrations: `python manage.py migrate`
4. Done!

## After deploy

After the deployment don't forget about notifying people in the team's Slack channel.
