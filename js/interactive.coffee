SELECT_MODEL = "Search for model"
OR_USE_STARS = "or use stars"
OR_USE_MODEL = "or search model"

phps = 'resources/main/load'
findAjax = (type, obj, call)->
	$.post(phps+type+'.php', obj, call)
	
window.getTable = (row)->return $(row).find('select').val()
findBrand = (row)->
	findAjax('Brands', {'tableName':getTable(row),'brand':like},(brands)->showBrands(row, brands))

window.nearestStar = (stars, row)->
	findAjax('ByStar', {'tableName':getTable(row),'star':stars},(res)->console.log(res))#row.find('td').last().html(res.power))
	
showBrands = (row, brands)->
	#don some

window.modelInput = ()->
	return $('<input>').addClass('model')
		.attr({type: 'text',value:SELECT_MODEL})
		.focusin(()->
			this.value = "" if this.value == SELECT_MODEL
		).focusout(()->
			this.value = SELECT_MODEL if !this.value
		).keyup(()->
			findBrands($(this).parents('tr'))
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
					stars[k].addClass('active') for k in [0..lj]
					nearestStar(lj, $($(this).parents('tr')))))
				
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
		.append($('<td>').html(0))
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
	
window.getModel = ()->
	model = []
	for row in $('.appliances-table')
		cols = rows.find('td')
		model.append({
			type: $(cols[0]).val()
			co2: parseInt($(cols[3]).html())
		})
	return model
