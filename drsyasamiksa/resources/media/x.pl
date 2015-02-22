#!/usr/bin/perl -w
my @files = @ARGV;
foreach my $f (@files) {
    my $newf = $f;
    $newf =~ s/JPG/jpg/;
    system("mv $f $newf");
    print "$newf\n";
}
