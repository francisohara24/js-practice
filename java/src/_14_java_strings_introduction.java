
public class _14_java_strings_introduction {
    public static void main(String[] args){
        String A = "hello";
        String B = "java";

        int sum = A.length() + B.length();
        System.out.println(sum);

        boolean isGreater = false;
        char[] charsA = A.toCharArray();
        char[] charsB = B.toCharArray();

        for(int i = 0; i < charsA.length; i++) {
            if(charsA[i]>charsB[i]) {
                isGreater = true;
                break;
            }
            else if(charsA[i]<charsB[i])
                break;
        }

        System.out.println(isGreater?"Yes":"No");

        System.out.println(A.substring(0,1).toUpperCase()+A.substring(1) + " " + B.substring(0,1).toUpperCase()+B.substring(1));

    }
}
