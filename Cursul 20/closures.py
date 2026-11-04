def make_mult_by_x(x):

    def mult_by_x(n):
        return n * x

    return mult_by_x

def add_html_tag(tag):

    def add_tag(content):
        return f'<{tag}>{content}</{tag}>'

    return add_tag

if __name__ == '__main__':
    # mult_by_2 = make_mult_by_x(2)
    # mult_by_3 = make_mult_by_x(3)
    # mult_by_10 = make_mult_by_x(10)
    # mult_by_100 = make_mult_by_x(100)
    #
    # for i in [1, 10, 15, 20, 3]:
    #     print(mult_by_2(i), mult_by_3(i), mult_by_10(i), mult_by_100(i))

    # Am aici un text -> <p>Am aici un text</p>
    make_html_paragraph = add_html_tag('p')
    make_html_header = add_html_tag('h1')
    print(make_html_paragraph("Am aici un text"))
    print(make_html_header("Am aici un alt text"))
    print(make_html_paragraph("Am aici o masina"))
