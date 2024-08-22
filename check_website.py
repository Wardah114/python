import os

def check_website_status(website):
    response = os.system(f"ping -c 1 {website}")

    if response == 0:
        print(f"{website} is online!")
    else:
        print(f"{website} is offline or unreachable.")

if __name__ == "__main__":
    # Replace 'example.com' with the website you want to check
    website = "example.com"
    check_website_status(website)
