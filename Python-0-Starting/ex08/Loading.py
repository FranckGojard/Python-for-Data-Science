def ft_tqdm(lst):
    """Display the progress of an iterable and yield its elements."""
    length = len(lst)
    for position, element in enumerate(lst):
        achieve = (position + 1) / length * 100
        bar_length = int(achieve / 100 * 100)
        bar = "=" * bar_length
        print(f"{achieve:.0f}%|{bar}| {position + 1}/{length}\r", end="")
        yield element