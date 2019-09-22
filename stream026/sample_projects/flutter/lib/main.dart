import 'package:flutter/material.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'Blank Flutter App',
      home: new MyHomePage(title: 'Blank Flutter App'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => new _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
        title: new Text(widget.title),
      ),
      body: new Container(),
      floatingActionButton: new Builder(builder: (context) {
        return new FloatingActionButton(onPressed: () {
          Scaffold.of(context).showSnackBar(
                new SnackBar(
                  backgroundColor: Colors.blue,
                  content: new Text('SnackBar'),
                ),
              );
        });
      }),
    );
  }
}
