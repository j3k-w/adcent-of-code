def check_transmission(layers: list) -> int:
    minn = 25 * 6
    m_idx = 0

    for idx, layer in enumerate(layers):
        if layer.count('0') < minn:
            minn = layer.count('0')
            m_idx = idx

    return layers[m_idx].count('1') * layers[m_idx].count('2')


def decode(layers: list):
    # 0 -> black
    # 1 -> white
    # 2 -> transparent
    final_layer = ''

    for layer in layers:
        for i in layer:
            if i == '0' or i == '1':
                final_layer += i
            else:
                break

    print(len(final_layer))

    return final_layer

if __name__=="__main__":
    with open('8input.txt') as f:

        # Preparing data.
        f = f.readline().strip()
        off = 25 * 6
        layers = [f[i:i+off] for i in range(0, len(f), off)]

        # First part.
        print(check_transmission(layers))

        # Second part.
        print(decode(layers))
