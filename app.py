'''
This is the main file of the web app.
'''
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, END
from arxiv_scraper import ArxivScraper
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Arxiv Paper Accumulator")
        self.domain_label = Label(root, text="Enter domains (comma-separated):")
        self.domain_label.pack()
        self.domain_entry = Entry(root)
        self.domain_entry.pack()
        self.interval_label = Label(root, text="Enter update interval (in minutes):")
        self.interval_label.pack()
        self.interval_entry = Entry(root)
        self.interval_entry.pack()
        self.search_button = Button(root, text="Search", command=self.search_papers)
        self.search_button.pack()
        self.papers_listbox = Listbox(root, width=100)
        self.papers_listbox.pack()
        self.filter_label = Label(root, text="Filter papers by domain:")
        self.filter_label.pack()
        self.filter_entry = Entry(root)
        self.filter_entry.pack()
        self.filter_button = Button(root, text="Filter", command=self.filter_papers)
        self.filter_button.pack()
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side="right", fill="y")
        self.papers_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.papers_listbox.yview)
        self.scraper = ArxivScraper()
    def search_papers(self):
        domains = self.domain_entry.get().split(",")
        interval = int(self.interval_entry.get())
        self.scraper.set_domains(domains)
        self.scraper.set_update_interval(interval)
        self.scraper.start()
    def filter_papers(self):
        domain = self.filter_entry.get()
        filtered_papers = self.scraper.filter_papers(domain)
        self.display_papers(filtered_papers)
    def display_papers(self, papers):
        self.papers_listbox.delete(0, END)
        for paper in papers:
            self.papers_listbox.insert(END, paper)
root = Tk()
app = App(root)
root.mainloop()