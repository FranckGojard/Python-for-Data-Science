def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for idx, i in enumerate(lst, start=1):
        progress = (idx / total) * 100
        print(f"\r{progress:.0f}%|", end='')
        len_bar = 50
        progress_bar = int((progress / 100) * len_bar)
        print(f"{'█' * progress_bar}{'.' * (len_bar - progress_bar)}| {idx}/{total}", end='')
        yield i
