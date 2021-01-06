<!-- $jsondata = fopen("json_dump.txt", "r")
$data = json_decode($jsondata, true);
DBName::insert($data);
     -->
Route::get('/insert-json-file-to-database-table', function(){
$json = file_get_contents(jsondump.json);
$objs = json_decode($json,true);
foreach ($objs as $obj)  {
    foreach ($obj as $key => $value) {
        $insertArr[str_slug($key,'_')] = $value;
    }
    DB::table('examples')->insert($insertArr);
}
dd("Finished adding data in examples table");
});