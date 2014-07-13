SELECT_MODEL = "Select model"
ROW_STRING = '<td>
		<select id="applianceType">
			<option value="airconditioner">Air conditioner</option>
			<option value="clothesdryer">Clothes dryer</option>
			<option value="computormonitors">Computor monitor</option>
			<option value="dishwashers">Dishwasher</option>
			<option value="fridgefreezer">Fridge/Freezer</option>
			<option value="television">Television</option>
		</select>
	</td>
	<td><input class="model" type="text" value="' + SELECT_MODEL + '"></input></td>
	<td><a class="use-stars-button" href="javascript:void(0);">or use energy stars</a></td>
	<td></td>'
	

	
addNewAppliance = ()->
	newRow = $('<tr>').html(ROW_STRING)
	newRow.find("input").focusin(()->
		this.value = "" if this.value == SELECT_MODEL
		).focusout(()->
			this.value = SELECT_MODEL if !this.value)
	$('.appliance-table').append(newRow)
		
$(document).ready ()->
	addNewAppliance()
	$('#addAppliance').click(addNewAppliance)
	
resultsReady = (val)->
	

			
