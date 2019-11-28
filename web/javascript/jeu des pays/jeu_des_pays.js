let les_pays = ['Afghanistan','Azerbaidjan','Kirghizistan', 'Pakistan', 'Tadjikistan', 'Turkmenistan', 'Ousbekistan'];
let bons_pays = [1, 5, 6, 0, 3, 4, 2];

function init(){
    let code='';
    let i, j;

    code+='<p>Retrouver les pays qui finissent par "stan"</p>\n';
    code+='<img src="carte.png" alt="carte des pays"></img>\n';
    code+='<br>';
    for (i = 0; i < les_pays.length; i++){
        code += '<div id="numero'+i+'">'+(i+1)+' - <select id="liste'+i+'" name="liste'+i+'"class="liste" onchange="selpays(this);"\n>';
        code += '<option value="" selected>...</option>\n';
        for (let pays in les_pays){
            code+= '<option value="pays'+i+'">' + les_pays[pays] +'</option>\n';
        }
        code+='</select></div>';
    }
    code+='<br><input type="button" value="Initaliser" onclick="init()"></input>\n';
    code+='<input type="button" value="Soumettre la réponse" onclick="verif()"></input>\n';
    document.body.innerHTML=code;
}

function verif(){
    let i, name;
    for (i=0; i < bons_pays.length; i++){
        let rep = document.getElementById('liste'+i).selectedIndex;
        console.log(rep);
        if (rep-1 == bons_pays[i]){
            document.getElementById('numero'+i).className="correct";
        }else{
            document.getElementById('numero'+i).className="incorrect";
        }
    }
}

function selpays(liste){
    //parcourir toutes les listes, verifier si ce n'est pas ma propre liste (celle d'appel) 
    //verifier si le selected index est different du mien et si il est egal au mien je mets le mien a 0 et afiche un message 
}