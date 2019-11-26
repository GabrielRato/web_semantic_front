function search_store(){
	var search_term = $('#search_term');
	var jqxhr = $.get(window.location.href+'/store/'+search_term, function() {
	    alert( "success" );
	  })
	  .done(function() {
	    alert( "second success" );
	  })
	  .fail(function() {
	    alert( "error" );
	  })
	  .always(function() {
	    alert( "finished" );
	  });
}
