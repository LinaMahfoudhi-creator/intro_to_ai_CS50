import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}
    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    links = corpus[page]
    random_value = random.random()
    if random_value >= damping_factor or not links:
        page = random.choice(list(corpus.keys()))
    else:
        # Choose a link at random from the current page
            page = random.choice(list(links))
    return page



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initialize PageRank values
    pagerank= dict()
    for page in corpus:
        pagerank[page] = 0

    # Start with a random page
    current_page = random.choice(list(corpus.keys()))
    # Sample n pages
    for iteration in range(n):
        # Increment the PageRank value for the current page
        pagerank[current_page] += 1 / n
        # Get the next page using the transition model
        current_page = transition_model(corpus, current_page, damping_factor)
    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {page: 1 / len(corpus) for page in corpus}
    convergence = False
    while not convergence:
        new_pagerank = {}
        for page in corpus:
            # Calculate the PageRank value for the current page
            rank_sum = 0
            for other_page in corpus:
                if page in corpus[other_page]:
                    rank_sum += pagerank[other_page] / len(corpus[other_page])
            new_pagerank[page] = (1 - damping_factor) / len(corpus) + damping_factor * rank_sum

        # Check for convergence
        convergence = all(abs(new_pagerank[page] - pagerank[page]) < 1e-6 for page in corpus)
        pagerank = new_pagerank

    return pagerank






if __name__ == "__main__":
    main()
