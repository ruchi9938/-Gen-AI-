import requests
import tkinter as tk

def fetch_messages_with_sources(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        if data['status'] == 'success':
            messages = data['data']['data']
            return messages
        else:
            print(f"Failed to fetch data: {data['message']}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def format_citations(messages):
    citations = []
    for message in messages:
        message_id = message['id']
        for source in message['source']:
            link = source.get('link', '')
            if link:
                citations.append({"id": message_id, "link": link})
    return citations

def display_citations_in_ui(citations):
    root = tk.Tk()
    root.title("Citations")

    label = tk.Label(root, text="Citations", font=("Helvetica", 16))
    label.pack(pady=10)

    listbox = tk.Listbox(root, font=("Helvetica", 12), selectmode=tk.BROWSE)
    listbox.pack(fill=tk.BOTH, expand=True)

    for citation in citations:
        listbox.insert(tk.END, f"ID: {citation['id']}, Link: {citation['link']}")

    root.mainloop()

# Example usage
url = 'https://devapi.beyondchats.com/api/get_message_with_sources?page=1'
messages = fetch_messages_with_sources(url)
citations = format_citations(messages)
display_citations_in_ui(citations)
