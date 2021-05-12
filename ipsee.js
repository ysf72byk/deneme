<script type="text/javascript">
function ZiyaretciBilgileri() {

  var text = ""

//Referel Bilgisi için (document.referrer)
 text += "Referrel Site = " + document.referrer;

  //Ekran Çözünürlülük Bilgisi: (screen.width ve screen.height)
  text += " ; Ekran Çözünürlülügü= " + screen.width + "X" + screen.height;

  //Browser Type : (navigator.appName)
 text += " ; Browser Tipi=" + navigator.appName;

  //Browser Version : (navigator.appVersion)
 text += " ; Browser Version=" + navigator.appVersion;

  //IP adress:
//.net için ip = '<%= Request.UserHostAddress%>';
 text += " ; IP Adresi=" + '<%= Request.UserHostAddress%>';
 alert(text);

}
</script>
