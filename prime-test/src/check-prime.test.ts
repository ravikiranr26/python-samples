/**
 * Prime Numbers:
 * Prints all the numbers which are greater than X and lesser than Y
 */

describe('Prime Number()', () => {

    let checkIsPrime;

    beforeEach(() => {
        checkIsPrime = jest.fn();
        checkIsPrime.mockImplementation((x, y) => {
            // returns prime numbers that are both bigger than X and smaller than Y
        });
    });

    test('should be called with a non-null argument', () => {
        // This assertion covers check when agrument is not undefined and null
        expect(checkIsPrime).toBeCalledWith(expect.anything());
    });

    test('should have arguments as two integers', () => {
        // Test to check if the two agruments are Integer:
        expect(typeof checkIsPrime(1, 2).mock.calls[0][0]).toBe('number')
        expect(typeof checkIsPrime(2, 4).mock.calls[0][1]).toBe('number');
    });

    test('should not have arguments as strings and non-integers, floats', () => {
        // Test that we get the right errors messages when the arguments are not integer:
        expect(checkIsPrime('a', 'b')).toThrowError(new Error('arguments need to be integer'));
        expect(checkIsPrime('a', -1)).toThrowError(new Error('arguments need to be integer'));
        expect(checkIsPrime(0, -1)).toThrowError(new Error('arguments need to be integer'));
        expect(checkIsPrime(-1, -1)).toThrowError(new Error('arguments need to be integer'));
        expect(checkIsPrime('', '')).toThrowError(new Error('arguments need to be integer'));
        expect(checkIsPrime()).toThrowError(new Error('arguments missing'));
        expect(checkIsPrime(0.34, 12.23)).toThrowError(new Error('arguments need to be integer'));
        expect(checkIsPrime(-1, 20)).toThrowError(new Error('arguments need to be integer'));
    });

    test('should have arguments such that x is less than y to function', () => {
        // Test to check wheather the function is initiated only once'
        expect(checkIsPrime(8, 21)).toHaveBeenCalledWith(8, 21);
        expect(checkIsPrime).toHaveBeenCalledTimes(1);

        expect(checkIsPrime(21, 8)).toHaveBeenNthCalledWith(21, 8);
        expect(checkIsPrime).toHaveBeenCalledTimes(0);

        expect(checkIsPrime(21, 21)).toHaveBeenNthCalledWith(21, 21);
        expect(checkIsPrime).toHaveBeenCalledTimes(0);

        expect(checkIsPrime(0, 1)).toHaveBeenNthCalledWith(0, 1);
        expect(checkIsPrime).toHaveBeenCalledTimes(0);
    });

    test('should print all prime numbers only, bigger than arg1 and smaller than arg2', () => {
        // Test to verify the correct return of prime numbers for all different valid inputs cases
        expect(checkIsPrime(1, 10)).toHaveReturnedWith('2, 3, 5, 7');
        expect(checkIsPrime(11, 29)).toHaveReturnedWith('13, 17, 19, 23');
        expect(checkIsPrime(97, 100)).toHaveReturnedWith('no prime numbers found');
        expect(checkIsPrime(41, 43)).toHaveReturnedWith('no prime numbers found');
        expect(checkIsPrime(2, 7)).toHaveReturnedWith('3, 5');
        expect(checkIsPrime(0, 1)).toHaveReturnedWith('no prime numbers found');
    });

});