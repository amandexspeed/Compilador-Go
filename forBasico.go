package testeCompilador

var (
    a int
    b string
    c bool
)

func main() {
	i := 0
	for i<10 {
		i++
	}	
	funcif()

}
func funcif(){

	i,j:=0,1;
	if (true){
		if(i==0){
			i++;
		}else{
			i--;
		}
	}
	j = i + 1;
	i = j
}