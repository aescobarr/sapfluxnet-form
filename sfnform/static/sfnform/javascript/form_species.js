function getUlLiIndex(){
	return $("#sp_list ul.species li").size();
}
function addSp(){
	var species_name = $("#entrada_sp").val();
	if(species_name && species_name.trim()!=''){
		doAdd(species_name);
		updateSpListValue();
	}else{
		alert("Please enter the name of the species and click the add button");
	}
}
function doAdd(species){
	var index = getUlLiIndex();				
	$("#sp_list ul.species").append('<div id="sp_' + index + '_div" class="text-right col-md-1"></div><li id="sp_' + index + '_li">' + species + '<button type="button" onclick="removeSp(' + index + ')"><span class="glyphicon glyphicon-remove"></span></button></li>');
}
function removeSp(index){
	$('#sp_' + index + '_div').remove();
	$('#sp_' + index + '_li').remove();
	updateSpListValue();
}
function updateSpListValue(){
	var species = [];
	$("#sp_list ul.species li").each(
		function(index){
			species.push($(this).text().trim());
		}
	);
	var species_string = species.join(";");
	$('#id_species').val(species_string);
}
function rebuildUi(val){
	var sp = val.split(";");	
	if(sp && sp!=''){
		for(var i = 0; i<sp.length;i++){
			doAdd(sp[i]);
		}
	}	
}
jQuery( document ).ready(function( $ ) {
	var species_value = $('#id_species').val();
	rebuildUi(species_value);
});