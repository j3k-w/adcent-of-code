def decode(f: str):
    off = 25 * 6

    layers = [f[i:i+off] for i in range(0, len(f), off)]

    minn = off
    minn_idx = 0

    for idx, layer in enumerate(layers):
        if layer.count('0') < minn:
            print(f"found less zeros at {idx} layer")
            minn = layer.count('0')
            minn_idx = idx

    result = layers[minn_idx].count('1') * layers[minn_idx].count('2')

    return result


if __name__=="__main__":
    with open('8input.txt') as f:
        f = f.readline().strip()

        print(decode(str(f)))
