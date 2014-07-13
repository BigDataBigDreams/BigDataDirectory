SELECT_MODEL = "Search for model"
USE_STARS = "or use stars"
USE_MODEL = "or search model"

modelInput = ()->
	return $('<input>').addClass('model')
		.attr({type: 'text',value:SELECT_MODEL})
		.focusin(()->
			this.value = "" if this.value == SELECT_MODEL
		).focusout(()->
			this.value = SELECT_MODEL if !this.value
		)

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
		.append($('<td>').html(modelInput()))
		.append($('<td>').append($('<a>')
			.html(USE_STARS)
			.attr('href', "javascript:void(0);")
			.addClass('use-stars-button')
			.click(()->
				jthis = $(this)
				if jthis.html() == USE_STARS
					jthis.html(USE_MODEL)
					newRow.find('.input').html(modelInput())
				else
					jthis.html(USE_STARS)))
					newRow.find('.input').html(getStarInput()))
		.append($('<td>'))
		return newRow

getStarInput = ()->
	starspan = $('<span>').addClass('stars')
	stars = []
	for j in [0...6]
		_j = j
		stars.push($('<span>')
			.click(()->
				for k in [0.._j]
					stars[k].addClass('active')
				for k in [_j+1...6]
					stars[k].removeClass('active')))
	return starspan
	
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
