import subprocess


def run_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line.strip())

        process.communicate()  # Wait for the process to complete
        return_code = process.returncode

        if return_code == 0:
            print("Command executed successfully!")
        else:
            print(f"Command failed with return code: {return_code}")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing the command: {e}")
        print("Error output:")
        print(e.stderr)


if __name__ == "__main__":
    access_key = "rj0OFc/hUm5MFLOWhn8Hf86ZcnlyBrdi16GhijXt"

    pages = [
        {'ko-notice': 'https://mooda.notion.site/15aca483507d4197981005b894e86777'},
        {'en-notice': 'https://mooda.notion.site/Notice-fad497e43d3140cc9b1fcf568318604c'}
        # {'ko-terms': 'https://mooda.notion.site/085a7d5cfdd14053b17b044f3f4b77d0'},
        # {'en-terms': 'https://mooda.notion.site/Terms-of-Use-14fb944b43f041d8b3ee87bffd118692'},
        # {'ko-privacy': 'https://mooda.notion.site/0a2a72510bb84330aff434cbef553ac2'},
        # {'en-privacy': 'https://mooda.notion.site/Privacy-Policy-8a967f1833e44048bd65094f670f7cfa'},
        # {'ko-faqs': 'https://mooda.notion.site/f32ad80a08934e6cafe0f2048ff33b69'},
        # {'en-faqs': 'https://mooda.notion.site/FAQs-43399dd642dd4728a51994d8f08cbd95'},
        # {'ko-community-guide': 'https://mooda.notion.site/3779d8000639421db4330643aa6e969d'},
        # {'en-community-guide': 'https://mooda.notion.site/Community-Guidelines-c1b058a8bc0b45eeb1502b2e9c2bf128'},
        # {'ja-community-guide': 'https://mooda.notion.site/44aacad36fa54512abaf217a08e5d292'},
        # {'th-community-guide': 'https://mooda.notion.site/933e1cec751f476fbc23fcabbd995952'},
        # {'zt-community-guide': 'https://mooda.notion.site/4d6e864c443d41ca904ad936e50c4b7f'},
        # {'zs-community-guide': 'https://mooda.notion.site/5b174548a2ed451783ce6f7529edb579'},
        # {'id-community-guide': 'https://mooda.notion.site/Panduan-Komunitas-be9f454b05a54a0ebe0aabbb6db3c2ae'}
    ]

    for page in pages:
        page_name, page_url = list(page.items())[0]
        command_to_run = f'python loconotion {page_url} --clean --page={page_name} --key={access_key}'
        run_command(command_to_run)
