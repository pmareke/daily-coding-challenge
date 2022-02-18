from sum import Sum
from mamba import description, it
from expects import expect, be_true, be_false

with description('Sum#upTo') as self:
    with it('two numbers up to'):
        sum = Sum([10, 7, 1])
        expect(sum.upTo(17)).to(be_true)

    with it('two numbers not up to'):
        sum = Sum([10, 1])
        expect(sum.upTo(17)).to(be_false)
