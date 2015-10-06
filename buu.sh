wget -q -U "Mozilla/5.0" --post-file output.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com.mx/speech-api/v2/recognize?output=json&lang=es&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"   | cut -d\" -f8  > stt.txt
 
value=`cat stt.txt`
echo "$value"
