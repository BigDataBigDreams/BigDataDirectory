SELECT_MODEL = "Search for model"
OR_USE_STARS = "or use stars"
OR_USE_MODEL = "or search model"

window.modelInput = ()->
	return $('<input>').addClass('model')
		.attr({type: 'text',value:SELECT_MODEL})
		.focusin(()->
			this.value = "" if this.value == SELECT_MODEL
		).focusout(()->
			this.value = SELECT_MODEL if !this.value
		)

window.getStarInput = ()->
	starspan = $('<span>').addClass('stars')
	stars = []
	for j in [0...6]
		do ()->
			lj = j
			stars.push($('<span>')
				.click(()->
					star.removeClass('active') for star in stars
					stars[k].addClass('active') for k in [0..lj]))
				
	return starspan.append(stars)
	
window.getNewRow = ()->
	newRow = $('<tr>')
		.append($('<td>').html(
			'<select id="applianceType">
				<option value="">Select appliance</option>
				<option value="airconditioner">Air conditioner</option>
				<option value="clothesdryer">Clothes dryer</option>
				<option value="computormonitors">Computor monitor</option>
				<option value="dishwashers">Dishwasher</option>
				<option value="fridgefreezer">Fridge/Freezer</option>
				<option value="television">Television</option>
			</select>'))
		.append($('<td>').addClass('input').html(modelInput()))
		.append($('<td>').append($('<a>')
			.html(OR_USE_STARS)
			.attr('href', "javascript:void(0);")
			.addClass('use-stars-button')
			.click(()->
				jthis = $(this)
				if jthis.html() == OR_USE_MODEL
					jthis.html(OR_USE_STARS)
					newRow.find('.input').html(modelInput())
				else
					jthis.html(OR_USE_MODEL)
					newRow.find('.input').html(getStarInput()))))
		.append($('<td>'))
	return newRow
	
addNewAppliance = ()->		
	$('.appliance-table').append(getNewRow())
		
$(document).ready ()->
	addNewAppliance()
	$('#addAppliance').click(addNewAppliance)


window.resultsReady = do ()->
	res = false
	return (val)->
		res = val
		if res
			$('.navbox li').addClass('navigable')
		else
			$('.navbox li').removeClass('navigable')
		return res
