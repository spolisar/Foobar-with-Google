public class Solution{
    // Start of the string "2357111317192329..."
    // since the index will be between 0 and 10000 the string
    // should be built from prime numbers from 0 to 10005
    // private static int upperBound = 100005;
    // private static int upperBound = 20231;
    private static int upperBound = 22000;
    private static StringBuilder primeString = buildPrimeString(upperBound);
    
    /**
     * Returns the next five digits in the string of all 
     * primes starting at i in the string
     * with i being between 0 and 10000
     * @param   i index of the string of all primes 
     * @return  five character string of digits from the string of all primes
     */
    public static String solution(int i) {
        // System.out.println(primeString.substring(10000));
        return primeString.substring(i, i+5);
    }
    
    /**
     * builds the prime string using the sieve of eratosthenes
     */
    private static StringBuilder buildPrimeString(int n){
        boolean primes[] = new boolean[n+1];
        for (int i=0; i<= n; i++){
            primes[i] = true;
        }
        
        for (int i=2; i*i <= n; i++){
            if (primes[i] == true){
                for (int j=i*i; j <= n; j+=i){
                    primes[j] = false;
                }
            }
        }
        
        StringBuilder primeStringBuilder = new StringBuilder();
        for (int i=2; i<= n; i++){
            if (primes[i] == true){
                primeStringBuilder.append(i);
            }

            if (primeStringBuilder.length() >= 10005){
                System.out.println(i);
                break;
            }
        }
        return primeStringBuilder;
    }

    public static void main(String[] args) {
        buildPrimeString(upperBound);
        System.out.println(primeString.substring(10000));
    }
}