timing_test(function() {
  at(0, function() {
    assert_styles('body', {'display':'none'});
  }, "Autogenerated");
  at(0.5, function() {
    assert_styles('body', {'display':'block'});
  }, "Autogenerated");
}, "Autogenerated checks.");