class node:
    def __init__(self, data, left, right):
        self.data = data
        self.right = right
        self.left = left


def recons(pre, mid):
    root = pre[0]
    i = mid.index(root)
    newleftmid = mid[:i]
    newrightmid = mid[i + 1:]
    newleftpre = pre[1:i + 1]
    newrightpre = pre[i + 1:]
    left = recons(newleftpre, newleftmid)
    right = recons(newrightpre, newrightmid)
    return node(root, left, right)


pre = ['A', 'B', 'D', 'E', 'C', 'F']
mid = ['D', 'B', 'E', 'A', 'F', 'C']

recons(pre, mid)
