#!/usr/bin/perl -w
use strict;
use CGI;
use CGI::Carp qw/warningsToBrowser fatalsToBrowser/;

# Creating a new CGI object.
my $query = new CGI;

my $first_name = $query->param("txt_first_name");
my $family_name = $query->param("txt_family_name");
my $email = $query->param("txt_email_name");
my $birthday = $query->param("txt_date_of_birthday");
my $favourite_sport = $query->param("cbo_favourite_sport");

print "Content-type:text/html\n\n";
print '<html>';
print '<head>';
print '<title>ICT373 CGI Results</title>';
print '</head>';
print '<body>';
print '<h3>Hello ICT373 Student.</h3>\n';
print '<span>Your CGI input variables were:</span>\n';
print "<span>First name: " , $first_name , "</span>\n";
#print "<span>Family name: " , $family_name , "</span>\n";
#print "<span>Email address: " , $email , "</span>\n";
#print "<span>Date of birth: " , $birthday , "</span>\n";
#print "<span>Favourite sport: " , $favourite_sport , "</span>\n";
print '</body>';
print '</html>';
