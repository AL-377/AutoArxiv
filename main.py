'''
This is the main file of the web app.
'''
from tkinter import Tk, Label, Entry, Button, Scrollbar, END, N, S, W, E
from tkinter.ttk import Treeview
from arxiv_scraper import ArxivScraper
import webbrowser

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Arxiv Paper Accumulator")

        self.domain_label = Label(root, text="Enter domains (comma-separated):")
        self.domain_label.grid(row=0, column=0, sticky=W)
        self.domain_entry = Entry(root)
        self.domain_entry.grid(row=0, column=1, sticky=W)

        self.interval_label = Label(root, text="Enter update interval (in minutes):")
        self.interval_label.grid(row=1, column=0, sticky=W)
        self.interval_entry = Entry(root)
        self.interval_entry.grid(row=1, column=1, sticky=W)

        self.search_button = Button(root, text="Search", command=self.search_papers)
        self.search_button.grid(row=2, column=0, columnspan=2)

        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.papers_treeview = Treeview(root, columns=("title", "abstract", "link"), show="headings", selectmode="browse")
        self.papers_treeview.heading("title", text="Title")
        self.papers_treeview.heading("abstract", text="Abstract")
        self.papers_treeview.heading("link", text="Link")
        self.papers_treeview.column("title", width=200, anchor="center")
        self.papers_treeview.column("abstract", width=300, anchor="center")
        self.papers_treeview.column("link", width=100, anchor="center")
        self.papers_treeview.grid(row=3, column=0, columnspan=2, sticky=(N, S, W, E))

        self.papers_treeview.columnconfigure(0, weight=1)
        self.papers_treeview.columnconfigure(1, weight=1)
        self.papers_treeview.columnconfigure(2, weight=1)

        self.scrollbar = Scrollbar(root)
        self.scrollbar.config(command=self.papers_treeview.yview)
        self.papers_treeview.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=3, column=2, sticky=(N, S))

        self.filter_label = Label(root, text="Filter papers by keyword:")
        self.filter_label.grid(row=4, column=0, sticky=W)
        self.filter_entry = Entry(root)
        self.filter_entry.grid(row=4, column=1, sticky=W)
        self.filter_button = Button(root, text="Filter", command=self.filter_papers)
        self.filter_button.grid(row=5, column=0, columnspan=2)

        self.scraper = ArxivScraper()

    def display_papers(self, papers):
        self.papers_treeview.delete(*self.papers_treeview.get_children())
        for paper in papers:
            title, abstract, link = paper.split("[SPLIT]")
            self.papers_treeview.insert("", "end", values=(title, abstract, link))

        self.papers_treeview.bind("<Double-1>", self.on_double_click)

    def on_double_click(self, event):
        item = self.papers_treeview.selection()[0]  # 获取选中的行
        link = self.papers_treeview.item(item, "values")[-1]  # 获取链接
        if link:
            webbrowser.open_new_tab(link)

    def search_papers(self):
        domains = self.domain_entry.get().split(",")
        interval = int(self.interval_entry.get())
        self.scraper.set_domains(domains)
        self.scraper.set_update_interval(interval)
        self.root.after(0, self.update_display,interval)

    def update_display(self,interval=None):
        self.scraper.scrape_papers()
        domain = self.filter_entry.get()
        if domain:
            filtered_papers = self.scraper.filter_papers(domain)
            self.display_papers(filtered_papers)
        else:
            self.display_papers(self.scraper.papers)
        self.root.after(interval * 60 * 1000, self.update_display,interval)

    def filter_papers(self):
        key_words = self.filter_entry.get().split(",")
        filtered_papers = self.scraper.filter_papers(key_words)
        self.display_papers(filtered_papers)

root = Tk()
app = App(root)
root.mainloop()