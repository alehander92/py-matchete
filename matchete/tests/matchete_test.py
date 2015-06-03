from matchete.on import on, Any, eq, is_in, not_eq, contains, matchable
import pytest


class TestOn(object):
    def test_decorating_methods(self):
        @matchable
        class A(object):
            @on(bool)
            def b(self, a):
                return 'bool'

            @on(int)
            def b(self, a):
                return 'int'

        a = A()
        assert a.b(2) == 'int'
        assert a.b(False) == 'bool'
        with pytest.raises(NotImplementedError):
            a.b('x')

    def test_matching_attributes(self):
        @matchable
        class B(object):
            @on('.a')
            def b(self, other):
                return 'a'

            @on('.hh')
            def b(self, other):
                return 'hh'

        @matchable
        class A(object):
            a = 2

        @matchable
        class Hh(object):
            hh = 4

        b = B()
        assert b.b(A()) == 'a'
        assert b.b(Hh()) == 'hh'
        with pytest.raises(NotImplementedError):
            b.b('x')

    def test_matching_lists(self):
        @matchable
        class A(object):
            @on([int])
            def join(self, elements):
                return ' '.join(str(e) for e in elements)

            @on([str])
            def join(self, elements):
                return ''.join(elements)

        a = A()
        assert a.join([2, 4]) == '2 4'
        assert a.join(['2', '4']) == '24'
        assert a.join([]) == ''
        with pytest.raises(NotImplementedError):
            a.join([2, 'x'])


    def test_matching_eq(self):
        @matchable
        class G(object):
            @on(eq('.nick', 'mariela'))
            def b(self, other):
                return 0

            @on(eq('.nick', 'krasimira'))
            def b(self, other):
                return 1

        @matchable
        class Woman(object):
            def __init__(self, nick):
                self.nick = nick

        mariela = Woman('mariela')
        krasimira = Woman('krasimira')
        g = G()

        assert g.b(mariela) == 0
        assert g.b(krasimira) == 1
        with pytest.raises(NotImplementedError):
            g.b(2)
