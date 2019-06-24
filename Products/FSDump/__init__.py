""" FSDump product intialization

$Id: __init__.py 105463 2009-11-03 14:52:27Z tseaver $
"""
import Dumper

def initialize( context ):

    context.registerClass( Dumper.Dumper
                         , constructors= ( ( 'addDumperForm'
                                           , Dumper.addDumperForm
                                           )
                                         , Dumper.addDumper
                                         )
                         , permission= 'Add Dumper'
                         , icon='www/dumper.gif'
                         )
